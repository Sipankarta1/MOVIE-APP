pipeline {
  agent any

  options { timestamps() }

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

          echo "Check eece430-4-5 dir:"
          if [ ! -d eece430-4-5 ]; then
            echo "eece430-4-5/ not found!"
            exit 1
          fi
          ls -la eece430-4-5

          echo "Show Dockerfile path:"
          if [ ! -f eece430-4-5/Dockerfile ]; then
            echo "Dockerfile not found at eece430-4-5/Dockerfile"
            exit 1
          fi
          ls -la eece430-4-5/Dockerfile
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
          # Build using Dockerfile inside eece430-4-5/ and context = eece430-4-5/
