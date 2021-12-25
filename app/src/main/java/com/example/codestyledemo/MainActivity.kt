package com.example.codestyledemo

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView


class MainActivity : AppCompatActivity(), View.OnClickListener {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        findViewById<TextView>(R.id.tv_to_java).setOnClickListener(this)

        val list = mutableListOf<Int>()
        for (i in 1..10) {
            list.add(i)
        }
    }

    override fun onClick(view: View?) {
        when (view!!.id) {
            R.id.tv_to_java -> {
                startActivity(Intent(this, JavaExampleActivity::class.java))
            }
        }
    }
}