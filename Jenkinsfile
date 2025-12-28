pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKERHUB_USER = 'tenyedi96'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t ${DOCKERHUB_USER}/incident-frontend:${IMAGE_TAG} -f dockerfile .'
                }
            }
        }
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t ${DOCKERHUB_USER}/incident-backend:${IMAGE_TAG} -f dockerfile .'
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh '''
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push ${DOCKERHUB_USER}/incident-frontend:${IMAGE_TAG}
                    docker push ${DOCKERHUB_USER}/incident-backend:${IMAGE_TAG}
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    ssh -i /var/lib/jenkins/.ssh/id_rsa -p 2233 udemx@192.168.1.167 \
                    "helm upgrade --install incident-logger /helm-charts/incident-logger-chart \
                     --set frontend.image=${DOCKERHUB_USER}/incident-frontend:${IMAGE_TAG} \
                     --set backend.image=${DOCKERHUB_USER}/incident-backend:${IMAGE_TAG}"
                '''
            }
        }
    }
    post {
        success {
            echo "Deployment successful! Build: ${IMAGE_TAG}"
        }
        always {
            sh 'docker logout'
        }
    }
}