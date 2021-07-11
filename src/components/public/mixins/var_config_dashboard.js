export default  {
	beforeMount(){
        this.set_dashboard_active()
	},
    methods: {
        set_dashboard_active(){
            this.axios.post("/var_config", {var_config: { var_config_id: 3, value: true}}).then(result => {
                console.log(result)
            }).catch(error => {
                console.log(error);
            })
            this.axios.post("/var_config", {var_config: { var_config_id: 1, value: false}}).then(result => {
                console.log(result)
            }).catch(error => {
                console.log(error);
            })
            this.axios.post("/var_config", {var_config: { var_config_id: 4, value: false}}).then(result => {
                console.log(result)
            }).catch(error => {
                console.log(error);
            })
        },
    }
}
