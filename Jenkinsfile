pipeline {
  agent any
  stages {
    stage('Build and Running') {
      steps {
        sh 'docker system prune -a'
        sh 'docker-compose down'
        sh ' docker-compose up --build -d'
        echo 'Success '
      }
    }

  }
}