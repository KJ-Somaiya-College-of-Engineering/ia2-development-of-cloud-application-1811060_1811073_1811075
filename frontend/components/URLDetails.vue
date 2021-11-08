<template>
  <div id="urlDetails" v-if="isLoading">
    <div
      class="columns is-multiline"
      style="padding: 10%; padding-top: 4%; padding-bottom: 0%"
    >
      <div class="column">
        <div class="card">
          <div class="card-content">
            <p class="loader title"></p>
          </div>
        </div>
      </div>
    </div>
    <div
      class="columns is-multiline"
      style="padding: 10%; padding-top: 0%; padding-bottom: 3%"
    >
      <div class="column">
        <div class="card" style="background-color: #ebfefc">
          <div class="card-content">
            <p class="title loader" style="color: #367362"></p>
            <p class="subtitle" style="color: #367362">Hits</p>
          </div>
        </div>
      </div>
      <div class="column">
        <div class="card" style="background-color: #ebfefc">
          <div class="card-content">
            <p class="title loader" style="color: #367362"></p>
            <p class="subtitle" style="color: #367362">
              <a target="_blank">
                <span class="icon is-small">
                  <i class="fas fa-external-link-alt"></i>
                </span>
              </a>
            </p>
          </div>
        </div>
      </div>
      <div class="column">
        <div class="card" style="background-color: #ebfefc">
          <div class="card-content">
            <p class="title loader" style="color: #367362"></p>
            <p class="subtitle" style="color: #367362">Time</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div id="urlDetails" v-else-if="!urlObject">
    <div class="notification is-danger is-light">
      Oops! Error Fetching Data. If this persists, contact developers.
    </div>
  </div>
  <div v-else>
    <div
      class="columns is-multiline"
      style="padding: 10%; padding-top: 4%; padding-bottom: 0%"
    >
      <div class="column">
        <div class="card">
          <div class="card-content">
            <p class="title" v-if="urlObject.title">
              {{ urlObject.title }}
            </p>
            <p class="title" v-else>
              Analytics for Your Shortened URL!
            </p>
            <a :href="urlObject.redirect_url" target="_blank">
              {{ urlObject.redirect_url }}
            </a>
          </div>
        </div>
      </div>
    </div>
    <div
      class="columns is-multiline"
      style="padding: 10%; padding-top: 0%; padding-bottom: 3%"
    >
      <div class="column">
        <div class="card" style="background-color: #ebfefc">
          <div class="card-content">
            <p class="title" style="color: #367362">
              {{ urlObject.hits }}
            </p>
            <p class="subtitle" style="color: #367362">Hits</p>
          </div>
        </div>
      </div>
      <div class="column">
        <div class="card" style="background-color: #ebfefc">
          <div class="card-content">
            <p class="title" style="color: #367362">
              trcr.tk/{{ urlObject._id }}&nbsp;
              <button class="button is-success is-outlined" v-on:click.prevent="copy(urlObject._id)">
                <span class="icon is-small">
                  <i class="fas fa-copy"></i>
                </span>&nbsp;&nbsp;&nbsp;{{ copyStatus }}
              </button>
            </p> 
            <p class="subtitle" style="color: #367362">
              Shortened URL
            </p>
          </div>
        </div>
      </div>
      <div class="column">
        <div class="card" style="background-color: #ebfefc">
          <div class="card-content">
            <p class="title" style="color: #367362">
              {{parsed(urlObject.created_ts ) }}
            </p>
            <p class="subtitle" style="color: #367362">Time</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import timeDiffernce from "@/functions/timeDifference";
export default {
  data() {
    return {
      errorFetching: false,
      copyStatus: 'Copy'
    };
  },
  computed: {
    isLoading() {
      return this.$store.state.isUrlDetailLoading;
    },
    urlObject() {
      return this.$store.state.activeUrlObject;
    },
  },
  methods: {
    copy(id) {
      this.$clipboard(`https://trcr.tk/${id}`);
      this.copyStatus = "Copied!"
    },
    parsed(created_ts) {
      if (created_ts == "Just Now") {
        return "Just Now";
      }
      var currentDate = new Date(created_ts * 1000);
      const tdiff = timeDiffernce(new Date(), currentDate);
      if (tdiff) return tdiff;
      const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];

      var date = currentDate.getDate();
      var month = currentDate.getMonth();
      var year = currentDate.getFullYear();

      return date + " " + monthNames[month + 1] + " " + year;
    },
  },
  mounted(){
    this.$store.dispatch("fetchSpecificUrl", this.$route.params.urlid);
  }
};
</script>

<style>
.loader {
  border: 6px solid #f3f3f3;
  border-radius: 50%;
  border-top: 6px solid #66d2b3;
  width: 30px;
  height: 30px;
  -webkit-animation: spin 2s linear infinite; /* Safari */
  animation: spin 2s linear infinite;
}

/* Safari */
@-webkit-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>