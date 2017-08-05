(function() {
  'use strict';

  angular.module('application', [
    'ui.router',
    'ngAnimate',
    'firebase',
    //foundation
    'foundation',
    'foundation.dynamicRouting',
    'foundation.dynamicRouting.animations'
  ]).controller("AppController", function($scope, $firebaseObject) {
      var ref = firebase.database().ref().child("data");
      // download the data into a local object
      var syncObject = $firebaseObject(ref);

      syncObject.$bindTo($scope, "data");

      $scope.username;
      $scope.password;
      $scope.status;
      $scope.pair;
      var error = 0;
      $scope.login = function(){
        firebase.auth().signInWithEmailAndPassword($scope.username, $scope.password).catch(function(error) {
        // Handle Errors here.
        console.log(error.code);
        console.log(error.message);
        // ...
        error = 1;
      });
      updateStatus();
      }

      $scope.logout = function(){
        firebase.auth().signOut().then(function() { updateStatus});
        updateStatus();
      }

      $scope.setMode = function(mode){
        $scope.data.mode = mode;
        console.log(syncObject.mode);
      }

      $scope.setPair = function(pair){
        if (pair===0){
          $scope.pair = "ETHUSD";
        }else if (pair===1){
          $scope.pair = "XBTUSD";
        }
        else if (pair===2){
          $scope.pair = "LTCUSD";
        }
        else if (pair===3){
          $scope.pair = "ETHXBT";
        }
        else if (pair===4){
          $scope.pair = "all";
        }
        $scope.data.crypto.pair = $scope.pair;
        console.log( syncObject.crypto);
      }

      var updateStatus = function(){
        var user = firebase.auth().currentUser;
        if (user) {
        // User is signed in
          $scope.status = "Logged in!";
          error = 0;
        } else {
          $scope.status = "Logged out";
        }
        if (error==1){
          error = "Incorrect username or password :(";
        }
      }
      updateStatus();

      

      console.log(syncObject);
    })
    .config(config)
    .run(run)
  ;

  config.$inject = ['$urlRouterProvider', '$locationProvider'];

  function config($urlProvider, $locationProvider) {
    $urlProvider.otherwise('/');

    $locationProvider.html5Mode({
      enabled:false,
      requireBase: false
    });

    $locationProvider.hashPrefix('!');
  }

  function run() {
    FastClick.attach(document.body);
  }

})();
