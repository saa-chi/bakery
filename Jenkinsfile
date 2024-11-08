pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                script {
                    // Use conditional logic to handle different OS environments
                    if (isUnix()) {
                        sh '''
                            python -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            call venv\\Scripts\\activate
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pytest
                        '''
                    } else {
                        bat '''
                            call venv\\Scripts\\activate
                            pytest
                        '''
                    }
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Deploying application..."
                            # Add your deployment commands here
                        '''
                    } else {
                        bat '''
                            echo Deploying application...
                            REM Add your deployment commands here
                        '''
                    }
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
