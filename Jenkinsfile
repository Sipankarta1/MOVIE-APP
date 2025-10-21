pipeline {
  agent any

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Sanity: Docker & Files') {
      steps {
        sh '''
          echo "DOCKER_HOST=${DOCKER_HOST:-unix:///var/run/docker.sock}"
          ls -l /var/run/docker.sock || true
          docker version

          echo "Repo tree (top-level):"
          ls -la

          echo "Check eece430-4-5
 dir:"
          ls -la eece430-4-5
 || { echo "eece430-4-5
/ not found!"; exit 1; }

          echo "Show Dockerfile path:"
          ls -la eece430-4-5
/Dockerfile || { echo "Dockerfile not found at eece430-4-5
/Dockerfile"; exit 1; }
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
          # Build using Dockerfile inside eece430/ and context = eece430-4-5
/
          docker build -f eece430/Dockerfile -t my-django-app:latest eece430-4-5

        '''
      }
    }

    stage('(Optional) Stop Old Container') {
      steps {
        sh '''
          docker rm -f my-django-app || true
        '''
      }
    }

    stage('Run New Container') {
      steps {
        sh '''
          docker run -d --name my-django-app -p 8000:8000 my-django-app:latest
        '''
      }
    }
  }
}
