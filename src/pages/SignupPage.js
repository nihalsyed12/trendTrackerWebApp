import React from 'react'
import Header from '../components/Header'
import Signup from '../components/Signup'

export default function SignupPage() {
  return (
    <>
    <Header 
      heading='Signup to Create and Account'
      paragraph = 'Already have an account'
      linkName='Login'
      linkURL='/'
    />
    <Signup />
    </>
  )
}
