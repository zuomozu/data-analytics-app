pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build('data-analytics-app:latest')
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
