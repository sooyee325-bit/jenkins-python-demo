pipeline {
    agent { 
        docker { image 'python:3.13' } 
    }
        
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


        stage('Verify Python') {
            steps {
                sh '''
                python3 --version || python --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv        # create a virtual environment in ./venv
                . venv/bin/activate         # activate it
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v test_app.py
                '''
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
