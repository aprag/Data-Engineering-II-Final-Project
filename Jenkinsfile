pipeline {
  agent any
  stages {
    stage('Build and Running') {
      parallel {
        stage('Build and Running') {
          steps {
            sh 'docker system prune -a'
            sh 'docker-compose down'
            sh ' docker-compose up --build -d'
            echo 'Success '
          }
        }

        stage('Test') {
          steps {
            sh 'cd tests'
            sh 'python -m pytest'
          }
        }

        stage('Off') {
          steps {
            sh 'docker-compose down'
            echo 'Sucess'
          }
        }

      }
    }

  }
}
