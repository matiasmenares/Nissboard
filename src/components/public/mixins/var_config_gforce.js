export default  {
	beforeMount(){
        this.set_gforce_active()
	},
    methods: {
        set_gforce_active(){
            this.axios.post("/var_config", {var_config: { var_config_id: 3, value: false}}).then(() => {
            }).catch(error => {
                console.log(error);
            })
            this.axios.post("/var_config", {var_config: { var_config_id: 1, value: true}}).then(() => {
            }).catch(error => {
                console.log(error);
            })
            this.axios.post("/var_config", {var_config: { var_config_id: 4, value: false}}).then(() => {
            }).catch(error => {
                console.log(error);
            })
        },
    }
}
