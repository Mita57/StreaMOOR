<template>
  <div class="sign-up mt-4">
    <h3>Давайте создадим новый аккаунт!</h3>
      <v-text-field type="text" v-model="email" placeholder="Адрес электронной почты"><br> </v-text-field>
    <v-text-field type="password" v-model="password" placeholder="Пароль"><br></v-text-field>
    <v-text-field type="password" v-model="passwordconf" placeholder="Повторите пароль"> <br></v-text-field>
    <v-btn x-large  @click="signUp" color="success" dark class="mt-4" to = "/sign-Up">Зарегистрироваться</v-btn>
    <span>Или вернуться к форме <router-link to="/login">авторизации</router-link>.</span>
  </div>
</template>

 <script>
  import firebase from 'firebase';
  export default {
    name: 'signUp',
    data() {
      return {
        email: '',
        password: '',
        passwordconf: '',
      }
    },
    methods: {
      signUp: function() {
        firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then(
          () => {
            this.$router.replace('home')
          },
          (err) => {
            alert('Oops. ' + err.message)
          }
        );
      }
    }
  }
</script>

 <style scoped>
  .sign-up {
      margin: auto;
      text-align: center;
      width: 50%;
  }
  input {
    margin: 10px 0;
    width: 20%;
    padding: 15px;
  }
  button {
    margin-top: 10px;
    width: 10%;
    cursor: pointer;
  }
  span {
    display: block;
    margin-top: 20px;
    font-size: 11px;
  }
</style>