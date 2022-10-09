<template>
  <div>
    <span>Moviehub</span>
    <el-divider></el-divider>
    <span>Pornhub</span>
  <div class="regis">
    Register
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="First Name" prop="firstname">
        <el-input v-model="ruleForm.firstname"></el-input>
      </el-form-item>
      <el-form-item label="Last Name" prop="lastname">
        <el-input v-model="ruleForm.lastname"></el-input>
      </el-form-item>
      <el-form-item label="Username" prop="username">
        <el-input v-model="ruleForm.username"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input v-model="ruleForm.password" show-password></el-input>
      </el-form-item>
      <el-button style="width:100px" @click="gologin" type="primary">Login</el-button>
      <el-button style="width:100px" @click="submit"  type="primary">Submit</el-button>
      <el-button @click="goreturn">Return</el-button>
    </el-form>
  </div></div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      ruleForm: {
        username: '',
        lastname:'',
        firstname:'',
        password:'',
      },
      rules: {
        username: [
          {required: true, message: 'Please input your username', trigger: 'blur'},
          {min: 1, max: 10, message: 'Between 1 and 10 characters in length.', trigger: 'blur'}
        ],
        lastname:[
          {required: true, message: 'Please input your lastname', trigger: 'blur'},
          {min: 1, max: 10, message: 'Between 1 and 10 characters in length.', trigger: 'blur'}
        ],
        firstname: [
          {required: true, message: 'please input your firstname', trigger: 'blur'},
          {min: 1, max: 10, message: 'Between 1 and 10 characters in length.', trigger: 'blur'}
        ],
        password:[
          {required: true, message: 'please input your password', trigger: 'blur'}
        ],
      }
    }
  },

  methods:{
    goreturn(){
      this.$router.go(-1)
    },
    gologin(){
      this.$router.push('/login')
    },
    submit(){
      this.$refs.ruleForm.validate((valid)=> {
        if(valid) {
          if(1) {
            this.$alert('You have successfully  registered.', 'Welcome', {
              confirmButtonText: 'Confirm',
            });
            this.$router.push('/login')
          }
          else{this.$alert('Two password does not match！')}
        }
      })
    },
  }
}
</script>

<style scoped>
.regis{
  -webkit-border-radius: 5px;
  border-radius: 5px;
  margin: 180px auto;
  width: 350px;
  padding: 35px 35px 15px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
</style>
