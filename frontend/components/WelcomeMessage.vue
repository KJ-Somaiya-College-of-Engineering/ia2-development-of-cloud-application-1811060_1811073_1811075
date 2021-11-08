<template>
    <div class="title is-2" style="font-family: 'Lobster', cursive; align: center;">
        Welcome to Dashboard, {{name}}!
    </div>
</template>

<script>
export default {
    computed: {
        name() {
            return this.$store.state.user?.NAME
        }
    }
}
</script>

<style>

</style>