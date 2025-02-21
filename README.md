# capstoneteam4 | Improving Intelligence Confidence

## Developer Installation
1. Setup SSH keys and clone the repository
```
git clone git@github.com:MemeDing/capstoneteam4.git
```
2. Initialize your Python virtual environment
    * **Linux:** Run *install-venv.sh*, then:
    ```
    source venv/bin/activate
    ```
    * **Windows:** Run *install-venv.bat*, then:
    ```
    venv/Scripts/activate
    ```

   * If Windows gives an error about your policy not allowing scripts to be run, open Powershell as an administrator and run this command:
   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Run the backend:
    * **Linux:** Run *run-backend.sh*
    * **Windows:** Run *run-backend.bat*

## Swagger Documentation / Testing
* Once the backend is running, navigate to http://127.0.0.1:3001/docs (or whatever IP and port you're running the backend on)

## Pull Requests
* When creating a Pull Request, there is a short pipeline that will run and check if the backend service runs properly.
* It will use the Linux scripts on a GitHub ubuntu machine to install and run the backend service, then run a GET request to check if /prompt/ and /history/ work properly.
* This ensures that the backend service still works properly and that the build scripts (for Linux) are functioning properly.
