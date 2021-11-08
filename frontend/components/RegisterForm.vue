<template>
  <div class="registerForm">
    <div class="notification is-success is-light" v-if="showSuccessNotification">
        Check Your Inbox!
    </div>
    <div class="notification is-danger is-light" v-else-if="showFailureNotification">
        Oops! Some Error. Try again in few minutes.
        <strong>If this persists, Contact Us!</strong>
    </div>
    <form v-else>
      <div class="field">
        <div class="control has-icons-left has-icons-right">
          <input class="input is-large" type="text" placeholder="Name" v-model="name" />
          <span class="icon is-small is-left">
            <i class="fas fa-user"></i>
          </span>
        </div>
      </div>
      <div class="field">
        <div class="control has-icons-left has-icons-right">
          <input class="input is-large" type="email" placeholder="Email" v-model="email"/>
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
        </div>
      </div>
      <div class="control">
        <button class="button is-large is-fullwidth is-primary is-loading" v-if="isLoading">
                <span class="icon is-small">
                    <i class="fas fa-magic"></i>
                </span>&nbsp;&nbsp;&nbsp;
                Get Me My Magic Link!
            </button>
            <button class="button is-large is-fullwidth is-primary" v-on:click.prevent="authenticate()" v-else>
                <span class="icon is-small">
                    <i class="fas fa-magic"></i>
                </span>&nbsp;&nbsp;&nbsp;
                Get Me My Magic Link!
            </button>
      </div>
    </form>
  </div>
</template>

<script>
import triggerSignup from '@/functions/triggerSignup'
export default {
  data() {
    return {
      email: "",
      name: "",
      isLoading: false,
      showSuccessNotification: false,
      showFailureNotification: false
    }
  },
  methods: {
    async authenticate() {
      this.isLoading = true;
      try {
        const response = await triggerSignup(this.name, this.email, this);
        this.email = "";
        this.name = "";
        if(response) this.showSuccessNotification = true;
        else this.showFailureNotification = true;
      } catch (error) {
        console.log(error);
        this.showFailureNotification = true;
      }
      this.isLoading = false;
    }
  }
};
</script>

<style>
</style>