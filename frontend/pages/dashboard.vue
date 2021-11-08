<template>
    <div>
        <div style="padding: 10%; padding-top: 3%; padding-bottom: 0%"><WelcomeMessage/></div>
        <hr/>
        <AddURL style="padding: 10%; padding-top: 0%; padding-bottom: 2%;"/>
        <hr/>
        <AllURLs style="padding: 10%; padding-top: 2%;"/>
    </div>
</template>

<script>
import AddURL from '@/components/AddURL'
import AllURLs from '@/components/AllURLs'
import WelcomeMessage from '@/components/WelcomeMessage'
export default {
    middleware: 'checkAuth',
    components: { AddURL, WelcomeMessage, AllURLs }
}
</script>

<style>
</style>