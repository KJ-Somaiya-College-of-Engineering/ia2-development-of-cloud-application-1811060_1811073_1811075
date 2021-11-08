<template>
<div class="columns">
        <div class="column is-one-fifths"></div>
        <div class="column is-three-fifths">
    <div style="padding:4%; padding-top: 20%; " v-if="isEnabled">
        <div class="title">Let's Get You In!</div>
        <div class="subtitle">We Don't Save Passwords. We Email You Magic Links which will Authenticate you in Single Click!</div>
        <RegisterForm/>
    </div>
    <div style="padding:4%; padding-top: 20%; " v-else>
        <div class="title">Sorry, Registrations are Closed!</div>
        <div class="subtitle">We are currently in Beta and still testing our Services. You can still fillup our Google Form, requesting Beta Access. We will get back to you in no time.</div>
        <a href="https://forms.gle/RYP4ginDfF96bJZ87" class="button is-primary is-outlined">Request Beta Access &nbsp;&nbsp;&nbsp;<span class="icon is-small">
                        <i class="fas fa-arrow-right"></i>
                    </span></a>
    </div>
    </div>
    <div class="column is-one-fifths"></div>
    </div>
</template>

<script>
import RegisterForm from '@/components/RegisterForm'

import checkRevAuth from '@/functions/checkRevAuth'

export default {
    data() {
        return{
            isEnabled: true
        }
    },
    components: { RegisterForm },
    mounted() {
        checkRevAuth(this)
    }
}
</script>

<style>

</style>