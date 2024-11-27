pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/milkyway2005/Pytest.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    def python = tool name: 'Python 3.8', type: 'Python'
                    sh "${python}/bin/pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def python = tool name: 'Python 3.8', type: 'Python'
                    sh "${python}/bin/pytest --junitxml=results.xml"
                }
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}
