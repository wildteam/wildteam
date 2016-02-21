'use strict';

/* Controllers */

function formController($scope, $http) {
    $scope.formData = {};

    // process the form
    $scope.registerForm = function() {
        var pa={'reName':$scope.reName,'rePassword':$scope.rePassword,'secondPassword':$scope.secondPassword,'reTel':$scope.reTel}
console.log(pa)
        $http({
            method  : 'POST',
            url     : 'http://112.240.191.230:8000/user/deal_register',
            params    : pa,// pass in data as strings
            headers : { 'Content-Type': 'application/x-www-form-urlencoded','Access-Control-Allow-Origin':'true','CORS_ORIGIN_ALLOW_ALL':'true'}  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function(data) {
                console.log(data);

                if (!data.success) {
                    // if not successful, bind errors to error variables
                    $scope.errorName = data.errors.name;
                    $scope.errorSuperhero = data.errors.superheroAlias;
                } else {
                    // if successful, bind success message to message
                    $scope.message = data.message;
                }
            });
    };
}
function MyCtrl1() {}
MyCtrl1.$inject = [];


function MyCtrl2() {
}
MyCtrl2.$inject = [];
