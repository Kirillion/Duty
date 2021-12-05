using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C_H_Test
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        public Form2(Faculty faculty)
        {
            InitializeComponent();
            this.faculty = faculty;
            button1.Text = "Изменить";
            textBox1.Text = faculty.Name;
        }

        Faculty faculty;

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {
                if (this.faculty == null)
                {
                    Faculty.ADD(textBox1.Text);

                }
                else
                {
                    Faculty.Updste((int)faculty.Id, textBox1.Text);
                }
                Close();
            }
            else
            {
                button1.Text = "Введи текст";
            }


        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }
    }
}
