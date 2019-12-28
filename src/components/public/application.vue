<template>
	<div class="disable-select">
		<v-header></v-header>
		<v-alert></v-alert>
        <router-view></router-view>
		<v-footer></v-footer>
	</div>
</template>
<script>
    import Header from "./components/v-header";
	import Footer from "./components/footer";
	import Alerts from "./components/alerts";
	export default {
		name: 'Application',
		components: {
            'v-header': Header,
			'v-footer': Footer,
            'v-alert': Alerts,
        }, mounted (){
			document.oncontextmenu =new Function("return false;")
		}
	}
</script>

<style>
#modal-login___BV_modal_outer_{
	z-index: 1060 !important;
}
body {
	overflow: hidden;
}
.disable-select {
    user-select: none; /* supported by Chrome and Opera */
   -webkit-user-select: none; /* Safari */
   -khtml-user-select: none; /* Konqueror HTML */
   -moz-user-select: none; /* Firefox */
   -ms-user-select: none; /* Internet Explorer/Edge */
}

* {
	cursor: none;
}
#selector {
    cursor: none;
}
html {
    overflow: scroll;
    overflow-x: hidden;
}
::-webkit-scrollbar {
    width: 0px;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
}
/* Optional: show position indicator in red */
::-webkit-scrollbar-thumb {
    background: #FF0000;
}
#app{
    background: url("../../../static/images/back.png") !important;
    background-size:     cover !important;
    background-repeat:   no-repeat !important;
	background-position: center center !important;
}
</style>
