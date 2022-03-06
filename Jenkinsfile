pipeline {
agent any
    stages {
        stage('Build and Running') {
            when {
                    branch 'develop'
                }
            steps {
                sh 'docker-compose up -d --build'

            }
        }
    }
}

