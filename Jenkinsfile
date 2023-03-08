pipeline {
    agent any
    stages {
        stage('analisis-codigo') {
            steps {
                sh 'flake8 --max-complexity=10 --max-line-length=100 .'
                sh 'echo "Ejecuta SonarQube"'
            }
        }
        stage('test') {
            steps {
                sh 'python3 manage.py test'
                sh 'echo "Pruebas de aceptación (behave y selenium)"'
            }
            
        }
        stage('build') {
            steps {
                sh 'echo "Cosas de construcción"'
                // sh 'python manage.py collectstatic --noinput'
            }
        }
        stage('despliegue-pre') {
            steps {
                sh 'echo "Despliegue a pre-producción"'
                // sh 'chmod +x deploy.sh'
                // sh './deploy.sh'
            }
        }

        stage('Revisión por QA') {
            steps {
                input "Desplegar en producción?"
            }
        }
        stage('despliegue-pro') {
            steps {
                sh 'echo "Despliegue a producción"'
                sh 'echo "Despliegue a producción"'
            }
        }
    }
    post {
        always {
            deleteDir() /* clean up our workspace */
        }
    }

}
chuckNorris()