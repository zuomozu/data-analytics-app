pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('data-analytics-app')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image('data-analytics-app').inside {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Push the Docker image to a Docker registry (if needed)
                    docker.withRegistry('https://my-registry.com', 'my-credentials-id') {
                        docker.image('data-analytics-app').push('latest')
                    }

                    // Deploy to Minikube
                    sh 'kubectl apply -f deployment.yaml'
                }
            }
        }
    }
}
