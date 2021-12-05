using System;
using System.Collections.Generic;
using System.Linq;

#nullable disable

namespace C_H_Test
{
    public partial class Faculty
    {
        public long Id { get; set; }
        public string Name { get; set; }

        public Faculty()
        {

        }

        public Faculty(int id, string name)
        {
            Id = id;

            Name = name;
        }

        static public void ADD(string name)
        {

            using (var context = new My_dbContext())
            {
                context.Faculties.Add(new Faculty(0, name));
                context.SaveChanges();
            }
        }

        static public List<Faculty> getAll()
        {
            List<Faculty> faculties = new List<Faculty>();

            using (var context = new My_dbContext())
            {
                faculties = context.Faculties.ToList();
            }

            return faculties;
        }


        static public void Updste(int id, string new_name)
        {
            using (var context = new My_dbContext())
            {
                var faculty = context.Faculties
                    .Where(c => c.Id == id)
                    .FirstOrDefault();

                faculty.Name = new_name;
                context.SaveChanges();

            }
        }

        static public void Deleted(int id)
        {
            using (var context = new My_dbContext())
            {
                var faculty = context.Faculties
                    .Where(c => c.Id == id)
                    .FirstOrDefault();

                context.Remove(faculty);
                context.SaveChanges();

            }
        }
    }
}
