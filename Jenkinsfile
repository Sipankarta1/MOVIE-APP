pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        cleanWs()
        checkout scm   // reuse the SCM + credentials configured in the job
      }
    }

    stage('Build Docker Image') {
  steps {
    // Use the Dockerfile and context inside eece430-4-5/
    sh 'docker build -f eece430-4-5/Dockerfile -t my-django-app:latest eece430-4-5'
  }
}


    stage('Stop Old Container') {
      steps {
        sh 'docker stop my-django-app || true'
        sh 'docker rm my-django-app || true'
      }
    }

    stage('Run New Container') {
      steps {
        sh 'docker run -d --name my-django-app -p 8000:8000 my-django-app:latest'
      }
    }
  }
}
