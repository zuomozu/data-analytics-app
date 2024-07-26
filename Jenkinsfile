pipeline {
    agent any

    stages {
        stage('Verify Python Installation') {
            steps {
                script {
                    bat '''
                    REM Check if Python is available at the specified path
                    SET PYTHON_PATH=C:\\Users\\zuhai\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe
                    IF EXIST "%PYTHON_PATH%" (
                        "%PYTHON_PATH%" --version
                        "%PYTHON_PATH%" -m pip --version
                    ) ELSE (
                        echo Python executable not found at %PYTHON_PATH%
                    )
                    '''
                }
            }
        }
    }
}
