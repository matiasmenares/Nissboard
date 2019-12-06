<template>
	<div>
		<v-header></v-header>
		<v-alert></v-alert>
        <router-view></router-view>
		<v-footer></v-footer>
	</div>
</template>
<script>
    import Header from "./components/header";
	import Footer from "./components/footer";
	import Alerts from "./components/alerts";
	export default {
		name: 'Application',
		components: {
            'v-header': Header,
			'v-footer': Footer,
            'v-alert': Alerts,
        }
	}
</script>

<style>
	#modal-login___BV_modal_outer_{
		z-index: 1060 !important;
	}
</style>
