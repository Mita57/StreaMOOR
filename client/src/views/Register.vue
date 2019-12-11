<template>
    <div class="sign-up mt-4">
        <h3>Давайте создадим новый аккаунт!</h3>
        <v-text-field type="text" v-model="nickname" id="nicknameReg" placeholder="Никнейм"><br></v-text-field>
        <v-text-field type="text" v-model="email" id="emailReg" placeholder="Адрес электронной почты"><br></v-text-field>
        <v-text-field type="password" v-model="password" id="passwordReg" placeholder="Пароль"><br></v-text-field>
        <v-text-field type="password" v-model="passwordconf" id="passwordConfReg" placeholder="Повторите пароль"><br>
        </v-text-field>
        <v-btn x-large tile dark class="blue mt-4 sas" @click="signUpValidation()">Создать аккаунт</v-btn>
        <div class="mt-3">{{result}}</div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Register",
        data() {
            return {
                email: '',
                password: '',
                passwordconf: '',
                nickname: '',
                birth_day: '',
                result: ''
            }
        },
        methods: {
            signUpValidation() {
                let nicknameFlag = false;
                let emailFlag = false;
                let passwordFlag = false;
                if (document.getElementById('nicknameReg').value.length > 4) {
                    nicknameFlag = true;
                    document.getElementById('nicknameReg').style.backgroundColor = '#303030';
                } else {
                    document.getElementById('nicknameReg').style.backgroundColor = 'darkred';
                    nicknameFlag = false;
                }
                if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.getElementById('emailReg').value)) {
                    emailFlag = true;
                    document.getElementById('emailReg').style.backgroundColor = '#303030';
                } else {
                    emailFlag = false;
                    document.getElementById('emailReg').style.backgroundColor = 'darkred';
                }
                if (document.getElementById('passwordReg').value.length >= 4 && document.getElementById('passwordReg').value == document.getElementById('passwordConfReg').value) {
                    passwordFlag = true;
                    document.getElementById('passwordReg').style.backgroundColor = '#303030';
                    document.getElementById('passwordConfReg').style.backgroundColor = '#303030';
                } else {
                    passwordFlag = false;
                    document.getElementById('passwordReg').style.backgroundColor = 'darkred';
                    document.getElementById('passwordConfReg').style.backgroundColor = 'darkred';
                }

                if (nicknameFlag && emailFlag && passwordFlag) {
                    signUp(document.getElementById('nicknameReg').value, document.getElementById('emailReg').value, document.getElementById('passwordReg').value);
                }

                async function signUp(nick, emaii, pwrd) {
                    let bodyFormData = new FormData();
                    bodyFormData.set('nickname', nick);
                    bodyFormData.set('email', emaii);
                    bodyFormData.set('password', pwrd);
                    console.log(bodyFormData);
                    await axios({
                        headers: {
                            'Access-Control-Allow-Origin': '*',
                            'Content-Type': 'application/json',
                        },
                        method: 'post',
                        url: 'http://localhost:5000/register',
                        data: bodyFormData,
                    }).then(function (response) {
                        console.log(response);
                        if (response.data.info != 'good') {
                            this.result = 'Данный пользователь уже зарегестрирован'
                        } else {
                            this.user = nick;
                            this.router.push('/hubs');
                        }
                    })
                        .catch(function (response) {
                            //handle error
                            console.log(response);
                            alert('Kernel panic: not sycning')
                        })

                }
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
    .sas{
        width:250px;
    }
</style>
