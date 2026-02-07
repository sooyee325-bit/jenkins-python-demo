pipeline {
    agent any
    
    environment {
        APP_ENV = "dev"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sooyee325-bit/jenkins-python-demo.git'
            }
        }

        stage('Run Python App') {
            steps {
                sh 'python3 --version'
                sh 'python3 app.py'
            }
        }
    }
    
    post {
        success {
            echo "✅ Build successful"
        }
        failure {
            echo "❌ Build failed"
        }
    }
}