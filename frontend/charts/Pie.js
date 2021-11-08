import { Pie } from "vue-chartjs";
export default {
  extends: Pie,
  props: ["data"],
  mounted() {
    this.renderChart(this.data, {
      borderWidth: "10px",
      hoverBackgroundColor: "red",
      hoverBorderWidth: "10px"
    });
  }
};