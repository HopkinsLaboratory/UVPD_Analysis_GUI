import git, os, sys, shutil, subprocess, stat, time

def Update_GUI_files(repo_url, root, ID_file, repo_SHA, delete_dir_function):
    '''Updates the .py files associated with the MobCal-MPI GUI. Inputs are the repo URL,  the directory where the GUI .py launcher is located, and a .txt file containing the SHA value of the user's local clone of the GUI.'''

    # Define the repository URL
    temp_dir = os.path.join(root, 'temp')

    # Remove the temporary directory if it exists
    if os.path.isdir(temp_dir):
        delete_dir_function(temp_dir)
    
    # Clone the GitHub repository to the temporary directory
    try: 
        repo = git.Repo.clone_from(repo_url, temp_dir, branch='master')
    except Exception as e: 
        print(f'Exception: {e}')
        print('Unable to access github to check for updates, likely due to lack of an internet connection...')
        answer = input('Do you wish to proceed using the current version (y/n)?')
        if answer == 'y':
            return
        else:
            raise KeyboardInterrupt('User has opted not to open the GUI without checking for updates. The GUI launcher will now be closed.')
    
    # A handy dictionary to hold the paths of the files to be updated for subsequent looping. Syntax is as follows- Path to local file : Path to cloned GitHub file

    update_files = {
        str(os.path.join(root, 'UVPD_GUI_Launcher.py')): str(os.path.join(temp_dir, 'GUI', 'UVPD_GUI_Launcher.py')), #GUI launcher
        str(os.path.join(root, 'Python', 'main.py')): str(os.path.join(temp_dir, 'GUI', 'Python', 'main.py')), #Main function .py file
        str(os.path.join(root, 'Python', 'Update.py')): str(os.path.join(temp_dir, 'GUI', 'Python', 'Update.py')), #Main function .py file
        str(os.path.join(root, 'Python', 'workflows.py')): str(os.path.join(temp_dir, 'GUI', 'Python', 'workflows.py')), #Main function .py file
    }
    
    #update process for Windows users
    if os.getenv('APPDATA') is not None:
        
        #create a python script to update the relevant files
        update_script_path = os.path.join(temp_dir, 'update.py')
        
        with open(update_script_path, 'w') as opf:
            opf.write('import os, sys\n')
            opf.write('import shutil\n')
            
            # Write the logic to update each file
            for local_path, github_path in update_files.items():
                #local_full_path = os.path.join(root, f'{local_path}')
                #github_full_path = os.path.join(temp_dir, 'GUI_V2', f'{github_path}')
                opf.write(f'if os.path.isfile(r"{local_path}"): os.remove(r"{local_path}")\n')
                opf.write(f'shutil.move(r"{github_path}", r"{os.path.dirname(local_path)}")\n')
            opf.write('sys.exit(0)')
            
            #ensure file updates; without this, users can encounter issues if the .py file is created on cloud services like OneDrive
            opf.flush()
            os.fsync(opf.fileno())
        
        time.sleep(5) #a short delay so that Cloud-based services have enough time to update.

        # Execute the update script and exit
        try:
            subprocess.Popen(['python', update_script_path], shell=True)

        except subprocess.SubprocessError as e:
            print(f'An subprocess error occurred while executing {update_script_path}: {e}')

        except Exception as e:
            print(f'An unexpected error occurred when trying execute {update_script_path}: {e}')

        with open(ID_file,'w') as opf:
            opf.write(repo_SHA)

        return
    
    #Update process for Linux users
    else:
        for local_path, github_path in update_files.items():
            # Similar to Windows, but using direct Python commands instead of writing to a script
            if os.path.isfile(local_path):
                os.remove(local_path)
            shutil.move(github_path, os.path.dirname(local_path))
            
        #Update the ID file
        with open(ID_file, 'w') as opf:
            opf.write(repo_SHA)

        return
