<template>
  <div>
    <div class="columns">
      <div class="column is-two-fifths">
        <div
          class="title maintext"
          style="padding-left:10%; padding-right:10%;"
        >Analytics on Clicks!!</div>
        <div
          class="subtitle subtext"
          style="padding-left:10%; padding-right:10%;"
        >An End-to-End URL Shortening Service, providing Super Smart Analytics Right On Your Dashboard.</div>
        <div class="buttons" style="padding-left:10%; padding-right:10%;" v-if="isLoggedIn">
          <nuxt-link :to="'/dashboard'" class="button is-primary is-large is-outlined">Dashboard ></nuxt-link>
        </div>
        <div class="buttons" style="padding-left:10%; padding-right:10%;" v-else>
          <nuxt-link :to="'/register'" class="button is-primary is-large is-outlined">Join Us!</nuxt-link>
          <nuxt-link :to="'/login'" class="button is-light is-large">Log in</nuxt-link>
        </div>
      </div>
      <div class="column is-three-fifths">
        <img src="../assets/images/home-banner.png" />
      </div>
    </div>
    <br>
            <div class="walkthrough">
      <p class="step">
        <font size="5px;">
          🚀&nbsp;
          <b>Shorten URL</b>
        </font>
        <br />Let's assume you are circulating a
        <b>Google Form</b>. All you need to do is
        <strong>Paste</strong> that URL on Dashboard, and get back a
        <strong>Shortend URL</strong>.
      </p>
      <p class="step">
        <font size="5px;">
          🗣&nbsp;
          <b>Promote Everywhere</b>
        </font>
        <br />Now, instead of sharing old URL,
        <strong>Share New, Shortend URL</strong>. Don't Worry, that URL will
        <b>Redirect your audience to your Original URL.</b>
      </p>
      <p class="step">
        <font size="5px;">
          📊&nbsp;
          <b>Stats Time!</b>
        </font>
        <br />That's It! You are now ready to
        <b>Monitor All the Clicks on URL, from everywhere on the Globe!!!</b>
      </p>
    </div>
    <br/>
    <br/>
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer";
export default {
  components: { Footer },
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    }
  },
};
</script>

<style>
.maintext {
  padding-top: 35%;
  font-family: "Lobster", cursive;
  font-size: 50px;
}

.developers {
  font-family: "Lobster", cursive;
  font-size: 35px;
}

.subtext {
  padding-left: 20%;
  font-family: "Open Sans Condensed", sans-serif;
  font-size: 25px;
}

.buttons {
  padding-left: 20%;
}

.heading {
  padding-top: 0%;
  padding-left: 5%;
  font-family: "Lobster", cursive;
  font-size: 40px;
  text-transform: capitalize;
}

.brains {
  padding:5%;
  padding-right: 10%;
  padding-left: 10%;
  padding-top: 0%;
}

.subtext {
  padding-left: 5%;
  font-family: "Open Sans Condensed", sans-serif;
  font-size: 25px;
}

#typed {
  font-family: "Open Sans Condensed", sans-serif;
  font-size: 35px;
  color: #479ca1;
}

.buttons {
  padding-left: 20%;
}
body {
  font-family: Helvetica;
}

.walkthrough {
  width: 70%;
  margin: auto;
}

.step {
  border-top: 2px dashed;
  border-color: rgb(72, 255, 0) !important;
  margin: 0;
  padding: 30px;
}

.step:nth-child(even) {
  border-left: 2px dashed;
  border-top-left-radius: 30px;
  border-bottom-left-radius: 30px;
  margin-right: 30px;
  padding-right: 0;
}

.step:nth-child(odd) {
  border-right: 2px dashed;
  border-top-right-radius: 30px;
  border-bottom-right-radius: 30px;
  margin-left: 30px;
  padding-left: 0;
}

.step:first-child {
  border-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}

.step:last-child {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
</style>