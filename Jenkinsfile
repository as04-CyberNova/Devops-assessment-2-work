pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Files Exist') {
            steps {
                script {
                    def htmlExists = fileExists 'index.html'
                    if (!htmlExists) {
                        error("index.html file not found in the repository!")
                    } else {
                        echo "index.html exists."
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Ensure Python 3 is available on the Jenkins agent
                sh '''
                if command -v python3 &>/dev/null; then
                    python3 test_form.py
                elif command -v python &>/dev/null; then
                    python test_form.py
                else
                    echo "Python is not installed. Please install Python to run tests."
                    exit 1
                fi
                '''
            }
        }
    }
    
    post {
        success {
            echo "All tests passed! The HTML form is valid and ready."
        }
        failure {
            echo "Tests failed. Please check the test script output."
        }
    }
}
