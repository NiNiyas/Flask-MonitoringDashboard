export function StatusCodeDistributionController($scope, $http, infoService, endpointService, menuService, formService, plotlyService) {
    menuService.reset('status_code_distribution');
    endpointService.reset();

    formService.setReload(function () {
        const endpointId = endpointService.info.id;

        $http.get('api/endpoint_status_code_summary/' + endpointId).then(function (response) {

            const config = {
                responsive: true,
                displayModeBar: true
            }

            const distribution = response.data.distribution;

            const statusCodes = Object.keys(distribution);

            const data = [{
                values: statusCodes.map(statusCode => distribution[statusCode]),
                labels: statusCodes,
                type: 'pie'
            }];

            $scope.error_requests = response.data.error_requests;

            plotlyService.react(data, config, 'chart');

            // Resize chart on window resize
            window.addEventListener('resize', function() {
                plotlyService.resize('chart');
            });
        });
    });

    formService.reload();
}