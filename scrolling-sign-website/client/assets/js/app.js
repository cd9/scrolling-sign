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
      $scope.username;
      $scope.password;
      $scope.status;
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


      // synchronize the object with a three-way data binding
      // click on `index.html` above to see it used in the DOM!
      syncObject.$bindTo($scope, "data");
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
