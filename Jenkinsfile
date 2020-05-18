pipeline {
    options {
    ansiColor('xterm')
  }
agent { label 'master' }
    stages {
        stage('Commit') {
        steps {
  //          withEnv([""CRED_ID=test-${env.environment.toLowerCase()}",]) {
            withCredentials([usernamePassword(credentialsId: "test-${env.environment.toLowerCase()}", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
      sh 'echo $USERNAME $PASSWORD'
       sh "echo ${env.environment}"
       wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm']) {
  sh 'echo "\033[32m Green \033[0m" something that outputs ansi colored stuff'
}
       
       ansiColor('xterm') {
  echo 'echo "\033[32m Green \033[0m" something that outputs ansi colored stuff'
}
       
       
      }
   }
}
                     
        stage('build') {
            steps {
                sh 'echo -e "Default e[106mLight cyan"'
                sh 'echo "checking maven version"'
                sh 'mvn --version'
                script {output = sh returnStdout: true, script: 'echo `env`'}
           
                
                

                
                println "================"
                //println(env.getEnvironment().each { name, value -> println "Name: $name -> Value $value" })
                println (env.JENKINS_HOME)
                println(env.getEnvironment())
                
                }
}

                
                
               /* script {
                for(variable in env.getEnvironment()) {
                println "-------"
                println(variable)
                }
  
  } */
                
                stage('curl') {
                    steps {
                        script {
                        def String retv = sh(script: 'curl -siL https://google.co.in | egrep -o "200 OK|HTTP/2 200"', returnStdout: true).trim() as String
                            println(retv)
                            /*
                            def sout  = sh(returnStdout: true, script: '''#!/bin/bash
                               ret=$(curl -siL https://google.co.in | egrep -o "200 OK|HTTP/2 200")
                                 echo "printing retv $ret"
                                if [ "$ret" == "200 K" ];then
                                        echo "up"
                                        exit 0
                                else
                                        echo "Down"
                                        exit 1
                                fi
                            '''.stripIndent())
                            println("-----")
                            println(sout) */
                            if(retv == "200 OK") {
                            println("ok")
                                def Accno = [
                         "L1": "123",
                         "L2": "456",
                         "L3": "789",
                              ]
                  println(Accno["${env.environment.toUpperCase()}"])
                        }

                        }
                    }
                }
        
                        
        post {
    success {
      echo 'sucess'
    }
  }
        
        
        
         post { 
        always { 
            echo 'I will always say Hello again!'
            
sh 'curl "https://api.GitHub.com/repos/hari1892/Devops/statuses/$GIT_COMMIT?access_token=ffe7700cdbeb09629de698f265a8f7d0c958c8a4" \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{\"state\": \"success\",\"context\": \"continuous-integration/jenkins-public-ci\", \"description\": \"Jenkins\", \"target_url\": \"https://d5425984.ngrok.io/job/pipeline-sonar/$BUILD_NUMBER/console\"}"'
        }
    }
                        
                    
        }
    }
