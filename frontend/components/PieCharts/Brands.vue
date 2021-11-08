<template>
  <div id="app">
    <OSChart :data="chartData"></OSChart>
  </div>
</template>

<script>
import OSChart from "~/charts/Pie";
export default {
    components: { OSChart },
    props: ["stats"],
    data() {
        return {
            chartData: {
                hoverBackgroundColor: "red",
                hoverBorderWidth: 10,
                labels: ["Vivo", "XiaoMi", "Asus", "Nokia", "Apple", "Motorola", "Samsung", "Others"],
                datasets: [
                    {
                        label: "Brands",
                        backgroundColor: ["#66d2b3", "#367362", "#1f4339", "#4aee53", "#04fe11", "#36f362", "#4afe53", "04ff11"],
                        data: this.stats,
                    },
                ],
            },
        };
    },
};
</script>

<style>
</style>