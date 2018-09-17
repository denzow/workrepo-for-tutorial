<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <router-link class="navbar-brand" to="/">Django</router-link>

    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <a class="nav-link" href="#">Register</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Login</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapActions } = createNamespacedHelpers('header');

export default {
  name: 'MyHeader',
  computed: {
    isLoggedIn() {
      return this.accountInfo !== null;
    },
    ...mapState(['accountInfo']),
  },
  methods: {
    ...mapActions(['fetchAccountInfo']),
  },
  created() {
    this.fetchAccountInfo();
  },
};
</script>

<style scoped>

</style>
