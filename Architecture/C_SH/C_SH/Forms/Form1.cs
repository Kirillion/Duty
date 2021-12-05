using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C_SH
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DataSearch();
        }

        private void DataSearch()
        {
            List<Faculty> faculties = Faculty.getAll();
            dataGridView1.DataSource = faculties;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Forms.Form2 form2 = new Forms.Form2();
            form2.ShowDialog();
            DataSearch();


        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count > 0)
            {
                Faculty faculty = new Faculty(Convert.ToInt32(dataGridView1.Rows[dataGridView1.CurrentCell.RowIndex].Cells[0].Value), Convert.ToString(dataGridView1.Rows[dataGridView1.CurrentCell.RowIndex].Cells[1].Value));

                Forms.Form2 form = new Forms.Form2(faculty);
                form.ShowDialog();
                DataSearch();
            }
                
           
            
        }

        private void button3_Click(object sender, EventArgs e)
        {

            if (dataGridView1.SelectedRows.Count > 0)
            {

                var index = Convert.ToInt32(dataGridView1.Rows[dataGridView1.CurrentCell.RowIndex].Cells[0].Value);

                Faculty.Deleted(index);
                DataSearch();
            }
           
            
            
        }
    }
}
