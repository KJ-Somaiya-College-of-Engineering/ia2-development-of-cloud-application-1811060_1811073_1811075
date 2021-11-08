<template>
  <div class="column is-one-quarter">
    <div class="card">
      <div class="card-content">
        <span class="icon is-small"> <i class="fas fa-battery-full"></i></span>
        &nbsp;
        <div class="tooltip">
          <strong>{{ dataObject.battery }}</strong>
          <span class="tooltiptext">
            Battery Status when link was visited.
          </span>
        </div>
        <br />
        <span class="icon is-small"> <i class="fas fa-map-pin"></i></span>
        &nbsp;
        <div class="tooltip">
          <strong>{{ dataObject.ipaddress }}</strong>
          <span class="tooltiptext">
            IP Address of Internet Service Provider
          </span>
        </div>
        <br />
        <span class="icon is-small">
          <i class="fas fa-map-marked-alt"></i
        ></span>
        &nbsp;
        <div class="tooltip">
          <strong>{{ dataObject.city }}</strong>
          <span class="tooltiptext">
            Lat: {{ dataObject.latitude }} <br />
            Lon: {{ dataObject.longitude }}
          </span>
        </div>
        <br />
        <span class="icon is-small"> <i class="fas fa-memory"></i></span>
        &nbsp;
        <div class="tooltip">
          <strong>{{ dataObject.availableRam }} GB Ram</strong>
          <span class="tooltiptext"> Amount of RAM on device. </span>
        </div>
        <br />
        <span class="icon is-small"> <i class="fas fa-laptop"></i></span>
        &nbsp;
        <div class="tooltip">
          <strong>{{ dataObject.brand }} {{ dataObject.device }}</strong>
          <span class="tooltiptext">
            Platform on Which Browser was Running
          </span>
        </div>
        <br />
        <span class="icon is-small"> <i class="fas fa-cogs"></i></span>
        &nbsp;
        <div class="tooltip">
          <strong>{{ dataObject.os }}</strong>
          <span class="tooltiptext"> OS of that Machine </span>
        </div>
        <br />
        <span class="icon is-small" v-if="dataObject.time">
          <i class="fas fa-clock" ></i
        ></span>
        &nbsp;
        <div class="tooltip" v-if="dataObject.time">
          <strong>{{ parsed(dataObject.time) }}</strong>
          <span class="tooltiptext">
            Time when the url was hit on this device
          </span>
        </div>
        <br />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    dataObject: {
      required: true,
      type: Object,
    },
  },
  methods: {
    parsed(UNIX_timestamp) {
      var a = new Date(UNIX_timestamp * 1000);
      var months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ];
      var year = a.getFullYear();
      var month = months[a.getMonth()];
      var date = a.getDate();
      var hour = a.getHours();
      var min = a.getMinutes();
      var sec = a.getSeconds();
      var time =
        date + " " + month + " " + year + " " + hour + ":" + min + ":" + sec;
      return time;
    },
  },
};
</script>

<style>
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 130px;
  background-color: rgba(0, 0, 0, 0.658);
  color: #fff;
  text-align: left;
  border-radius: 6px;
  padding: 5px;

  /* Position the tooltip */
  position: fixed;
  z-index: 1;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}

.very-small {
  font-size: 10px;
}
</style>