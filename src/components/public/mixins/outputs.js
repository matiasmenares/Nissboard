export default  {
    data(){
        return {
            channel_output: [],
            slots: [],
        }
    },
	beforeMount(){
        this.set_channel_output()
	},
    methods: {
        set_channel_output(){
            this.sockets.subscribe('channelOutput', (data) => {
                let response = []
                data.map(result => {
                    this.slots.map(slot => {
                        if(slot.channel_output_id == result.id)
                            response[slot.id] = result
                    })
                })
                var filtered = response.filter(el => el != null);
                this.channel_output = filtered
            })
        },
    }
}
