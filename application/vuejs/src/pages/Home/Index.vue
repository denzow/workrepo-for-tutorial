<template>
  <div class="home">
    <div class="row no-gutters">
      {{boardList}}
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapActions } = createNamespacedHelpers('home');

export default {
  name: 'home',
  computed: {
    ...mapState([
      'boardList',
    ]),
  },
  methods: {
    ...mapActions([
      'fetchBoardList',
    ]),
  },
  async created() {
    this.fetchBoardList();
  },
};
</script>
<style lang="scss" scoped>
  .home {
    padding-top: 1rem;
    align-items: center;
  }
  .no-gutters {
    margin:1rem;
    padding:0;
    .col,
    [class*="col-"] {
      margin: 0;
      padding:0.5rem 1rem;
    }
  }

</style>
