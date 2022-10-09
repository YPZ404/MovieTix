<template>
  <div>
    <span>moviehub</span>
    <el-divider></el-divider>
    <span>Pornhub</span>
    <div>
      <el-container>
       <el-main>
        <div class="logincon">
          Login
          <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="Username" prop="username">
              <el-input v-model="ruleForm.username"></el-input>
            </el-form-item>
            <el-form-item label="Password" prop="password">
              <el-input v-model="ruleForm.password" show-password></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="goregister">
                Sign in
              </el-button>
              <el-button type="primary" @click="gologin">
                Log in
              </el-button>
              <el-button @click="goreturn">Return</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-main>
    </el-container>
  </div>
</div>
</template>

<script>
export default {
  name: "Login",
  methods:{
    goreturn(){
      this.$router.go(-1)
    },
    goregister(){
      this.$router.push('/register')
    },
    gologin(){
      this.$refs.ruleForm.validate((valid)=>{
          if(valid){
            let data = {username: this.ruleForm.username,password: this.ruleForm.password}
            /*axios
              .post("api", data)
              .then((res) => {
                console.log(res);
                if(res.data.role == admin )
                this.$router.push({ path: "/admin" });
              })*/
            if(this.ruleForm.username === 'victor'&& this.ruleForm.password=== '4399')
            {
              this.$alert('You have successfully logged in.', 'Welcome', {
                confirmButtonText: 'Confirm',
              });
            }
            else {
              this.$alert('wrong password or email!')
            }
          }
        }
      )
    }
  },

  data(){
    return{
      ruleForm: {
        username:'',
        password:'',
      },
      rules: {
        username:[
          {required: true, message: 'Please input your password', trigger: 'blur'}
        ],
        password:[
          {required: true, message: 'Please input your password', trigger: 'blur'}
        ],
      }
    }
  }
}
</script>

<style scoped>

.logincon {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  margin: 180px auto;
  width: 400px;
  padding: 35px 35px 15px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
  left:400px;
}
</style>
