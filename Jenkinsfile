pipeline {
  agent any
  stages {
    stage('Build and Running') {
      steps {
        sh 'docker-compose down'
        sh 'sudo docker system prune -a'
        sh 'y'
        sh ' docker-compose up -d'
        echo 'Build proceed'
      }
    }

    stage('Test') {
      steps {
        sh 'cd tests'
        sh 'python3 -m pytest'
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