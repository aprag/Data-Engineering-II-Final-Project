pipeline {
  agent any
  stages {
    stage('Build and Running') {
      steps {
        sh 'docker system prune -a'
        sh 'yes'
        sh 'docker-compose down'
        sh ' docker-compose up --build -d'
        echo 'Success '
      }
    }

    stage('Test') {
      steps {
        sh 'cd tests'
        sh 'python -m pytest'
        echo 'Test suceed'
      }
    }

    stage('End process') {
      steps {
        sh 'docker-compose down'
        echo 'Suceed'
      }
    }

  }
}