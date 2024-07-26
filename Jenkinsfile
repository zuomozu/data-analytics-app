pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                bat '''
                apt install python3 -y
                    python --version
                    pip --version
                '''
            }
        }
        stage('Install Packages') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                bat 'echo Building...'
            }
        }
        stage('Test') {
            steps {
                script {
                    bat 'pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    bat 'docker build -t data-analytics-app:latest .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    bat 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
