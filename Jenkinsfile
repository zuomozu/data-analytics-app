pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Use bat for Windows batch command
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Use bat for running pytest
                    bat 'pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    // Docker build command can be the same
                    bat 'docker build -t data-analytics-app:latest .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Use bat for kubectl apply
                    bat 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
