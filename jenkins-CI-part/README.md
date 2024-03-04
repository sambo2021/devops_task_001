
kubectl create namespace jenkins
---------------------------------------------------------------------------------------------------------------------------------------------
jenkins:
admin
833f2f66683841e3852f977d5875021b
---------------------------------------------------------------------------------------------------------------------------------------------
very important if ur using jenkins behind proxy:
https://stackoverflow.com/questions/44711696/jenkins-403-no-valid-crumb-was-included-in-the-request
---------------------------------------------------------------------------------------------------------------------------------------------
for not connected to port 5000- jenkins-slave
https://stackoverflow.com/questions/60455410/jenkins-kubernetes-plugin-provided-port50000-is-not-reachable
---------------------------------------------------------------------------------------------------------------------------------------------
kubectl create secret docker-registry docker-credentials --docker-username=mohamedsambo --docker-password={{mydockerhubPassword}} --namespace jenkins
---------------------------------------------------------------------------------------------------------------------------------------------
CI_PIPELINE:JenkinsFile
pipeline {
    agent {
        kubernetes {
            yaml"""
apiVersion: v1
kind: Pod
metadata:
  name: kaniko
  namespace: jenkins
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    imagePullPolicy: Always
    command:
    - sleep
    args:
    - 9999999
    volumeMounts:
      - name: jenkins-docker-cfg
        mountPath: /kaniko/.docker
  volumes:
  - name: jenkins-docker-cfg
    projected:
      sources:
      - secret:
          name: docker-credentials
          items:
            - key: .dockerconfigjson
              path: config.json
               """
        }
    }
    
    stages {

        stage("Cleanup Workspace") {
          steps {
            cleanWs()
          }
        }

        stage("Checkout from SCM"){
                steps {
                    git branch: 'main', credentialsId: 'github', url: 'https://github.com/sambo2021/devops_task_001'
                }
    
        }

        stage('Build & Push with Kaniko') {
          steps {
            container(name: 'kaniko', shell: '/busybox/sh') {
              sh '''#!/busybox/sh
    
                /kaniko/executor --dockerfile `pwd`/docker-compose-part/Dockerfile --context `pwd`/docker-compose-part  --destination=mohamedsambo/flask-app:5.0.0
              '''
            }
          }
        }
    }
}
--------------------------------------------------------------------------------------------------------------------------------------------------